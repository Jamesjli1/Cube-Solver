import './styles/App.css' // import styles
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
