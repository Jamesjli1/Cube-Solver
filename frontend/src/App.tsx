// Not used right now
import { useState } from 'react'          // from react
import reactLogo from './assets/react.svg'// logos
import viteLogo from '/vite.svg'          // logos


import './styles/App.css' // import files
import TopBar from './components/layout/TopBar';
import SideBar from './components/layout/SideBar';
import CubeCanvas from './components/cubebox/CubeCanvas';

// Website layout
export default App;
function App() {
  return (
    <div className="app-layout">
      <TopBar />
      <div className="main-content">
        <CubeCanvas />
        <SideBar />
      </div>
    </div>
  );
}
