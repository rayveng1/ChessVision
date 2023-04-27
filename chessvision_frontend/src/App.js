import "./App.css";
import React from 'react';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route }
  from 'react-router-dom';
import Main from './pages/Main'
import Confirm from './pages/Confirm';
import Results from './pages/Results';

export default function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/Main' element={<Main />} />
        <Route path='/Confirm' element={<Confirm />} />
        <Route path='/Results' element={<Results />} />
      </Routes>
    </Router>



  );
}

export function Page() {

  <h1>
    This is our homepage!
  </h1>

}

