import './App.css'
import { useState } from 'react';
import Draggable from 'react-draggable';

interface BoxItem {
  id: number;
  type: string;
  position: {
    x: number;
    y: number;
  };
}

function App() {
  const [boxes, setBoxes] = useState<BoxItem[]>([]);

  const addBox = (type: string): void => {
    const newBox: BoxItem = {
      id: boxes.length,
      type: type,
      position: { x: 0, y: 0 }
    };
    setBoxes([...boxes, newBox]);
  };

  const handleDrag = (id: number, data: { x: number; y: number }) => {
    setBoxes(boxes.map(box => 
      box.id === id ? { ...box, position: data } : box
    ));
  };

  return (
    <div className="relative h-screen w-screen">
      {boxes.map((box) => (
        <Draggable
          key={box.id}
          position={box.position}
          onDrag={(_, data) => handleDrag(box.id, { x: data.x, y: data.y })}
        >
          <div className="absolute cursor-move bg-blue-500 p-4 rounded-lg">
            {box.type}
          </div>
        </Draggable>
      ))}
      
      <div className="fixed bottom-4 left-4 flex gap-2">
        <button onClick={() => addBox('search')}>Add Search</button>
        <button onClick={() => addBox('profile')}>Add Profile</button>
      </div>
    </div>
  );
}

export default App;
