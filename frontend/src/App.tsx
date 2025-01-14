import {BrowserRouter, Routes, Route, Link} from 'react-router-dom';
import './App.css'
import Home from './pages/Home.tsx'
import Searchbar from './pages/search.tsx';
import Navigation from './components/navigator.tsx'

function App() {
  return (
    <>
    <BrowserRouter>
      <div className='text-center'>
      <Link to="/" className='text-center'>SPIDERWEB!!!</Link>
      </div>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/search" element={<Searchbar />} /> 
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
