import {BrowserRouter, Routes, Route, Link} from 'react-router-dom';
import './App.css'
import Home from './pages/Home'
import Searchbar from './pages/search';
import Profile from './pages/profile'
import Navigation from './components/navigator'
import { UserProvider } from './components/profileContext';

function App() {
  return (
    <>
    <BrowserRouter>
      <UserProvider>
        <div className='text-center'>
        <Link to="/" className='text-center'>SPIDERWEB!!!</Link>
        </div>
        <Navigation />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<Searchbar />} /> 
          <Route path="/profile" element={<Profile />} /> 
        </Routes>
      </UserProvider>
    </BrowserRouter>
    </>
  );
}

export default App;
