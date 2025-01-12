import {BrowserRouter, Routes, Route} from 'react-router-dom';
import './App.css'
import Home from './pages/Home.tsx'
import Navigation from './components/navigator.tsx'

function App() {
  return (
    <>
    <h1 className='text-center'>SPIDERWEB!!!</h1>
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
