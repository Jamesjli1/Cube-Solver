// Not used right now
import { useState } from 'react'                // from react, to use in side panel logo later
import githubDLogo from './assets/githubdark.svg' // logos
import webLogo from '/turbocube.svg'           // logos


import './styles/App.css' // import files
import TopBar from './components/layout/TopBar';
import SideBar from './components/layout/SideBar';
import CubeCanvas from './components/cubebox/CubeCanvas';

// Website layout
export default function App() {
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
