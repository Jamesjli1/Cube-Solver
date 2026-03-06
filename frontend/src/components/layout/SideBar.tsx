// Code ui for the right side bar containing logic to switch state

import Button from '../ui/Button'; // Import button

export default function SideBar() {
  {/* To test clicking in console */}
  const handleTestClick = (move: string) => {
    console.log(`Button ${move} was clicked!`);
  };

  return (
    <aside className="sidebar">      
      <h3>Functions</h3>
      <div className="button-grid">
        <Button label="Scramble" onClick={() => handleTestClick('Scramble')} />
        <Button label="Reset" onClick={() => handleTestClick('Reset')} />
        <Button label="Create" onClick={() => handleTestClick('Create')} />
        <Button label="Scan" onClick={() => handleTestClick('Scan')} />
      </div>

      <div style={{ marginTop: '20px' }}>
        <Button label="Solve" onClick={() => alert('Generating Solution...')} />
      </div>

      <h3>Controls</h3>
      <div className="button-grid">
        <Button label="White CW" onClick={() => handleTestClick('WCW')} />
        <Button label="White CCW" onClick={() => handleTestClick('WCCW')} />
        <Button label="Yellow CW" onClick={() => handleTestClick('YCW')} />
        <Button label="Yellow CCW" onClick={() => handleTestClick('YCCW')} />
        <Button label="Blue CW" onClick={() => handleTestClick('BCW')} />
        <Button label="Blue CCW" onClick={() => handleTestClick('BCCW')} />
        <Button label="Green CW" onClick={() => handleTestClick('GCW')} />
        <Button label="Green CCW" onClick={() => handleTestClick('GCCW')} />
        <Button label="Red CW" onClick={() => handleTestClick('RCW')} />
        <Button label="Red CCW" onClick={() => handleTestClick('RCCW')} />
        <Button label="Orange CW" onClick={() => handleTestClick('OCW')} />
        <Button label="Orange CCW" onClick={() => handleTestClick('OCCW')} />
      </div>
    <div className="sidebar-footer">
        <p>© 2026 TurboCube by James Li</p>
        <p>Licensed under MIT</p>
      </div>
    </aside>
  );
}