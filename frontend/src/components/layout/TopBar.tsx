// Top bar including logo, github link, help info
import { useState } from 'react';
import githubLight from '../../assets/githublight.svg';
import githubDark from '../../assets/githubdark.svg';

export default function TopBar() {
  const [isDark, setIsDark] = useState(true); // Set theme to dark

  const handleHelpClick = () => {
    console.log("Help button clicked");
    // Future: what happens after help
  };

  const toggleTheme = () => {
    setIsDark(!isDark);
    console.log(`Theme switched to: ${!isDark ? 'dark' : 'light'}`);
    // Future: Theme toggle logic
  };

  return (
    <header className="topbar">
      {/* Left side with logo and name */}
      <div className="topbar-left">
        <img src="/turbocube.svg" alt="TurboCube Logo" className="app-logo" />
        <span className="brand-name">TurboCube</span>
      </div>
      
      {/* Right side with dark/light, github, help */}
      <div className="topbar-right">
        {/* 1. CSS Slider */}
        <div className={`theme-slider ${isDark ? 'dark' : 'light'}`} onClick={toggleTheme}>
          <div className="slider-circle"></div>
        </div>

        {/* 2. GitHub SVG Link */}
        <a 
          href="https://github.com/Jamesjli1/Cube-Solver" 
          target="_blank" 
          rel="noopener noreferrer"
          className="topbar-link"
        >
          <img 
            src={isDark ? githubDark : githubLight} 
            alt="GitHub" 
            className="github-icon" 
          />
        </a>

        {/* 3. CSS Help Button */}
        <button 
          className={`help-btn ${isDark ? 'help-dark' : 'help-light'}`} 
          onClick={handleHelpClick}
        >
          ?
        </button>
      </div>
    </header>
  );
}