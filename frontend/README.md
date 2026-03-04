To run:
cd frontend
npm install
npm run dev
go to localhost 

frontend/
├── src/
│   ├── api/               # THE BRIDGE
│   │   └── client.ts      # Axios/Fetch functions to call FastAPI
│   │
│   ├── cube/              # THE BRAIN (Pure TypeScript)
│   │   ├── state.ts       # Current 54-char string (UUU...RRR)
│   │   └── moves.ts       # Local math for instant turns (U, R, L)
│   │
│   ├── components/
│   │   ├── layout/        # THE SHELL (Static)
│   │   │   ├── TopBar.tsx      # Header/Title
│   │   │   └── Sidebar.tsx     # Container for the panels
│   │   │
│   │   ├── cube/          # THE 3D VIEW (Canvas)
│   │   │   └── CubeCanvas.tsx  # The box containing the 3D cube
│   │   │
│   │   ├── panels/        # THE SIDEBAR CONTENT (Swappable)
│   │   │   ├── MainMenu.tsx      # "Home" (Solve, Scramble buttons)
│   │   │   ├── SolvePanel.tsx    # Shows solution from Backend
│   │   │   ├── ScramblePanel.tsx # Shows scramble from Backend
│   │   │   ├── ScanPanel.tsx     # Opens scanner
│   │   │   └── CreatePanel.tsx   # Color picker + "Done" button
│   │   │
│   │   └── ui/            # THE TOOLS (Small parts)
│   │       └── Button.tsx      # Reusable styled button
│   │
│   ├── styles/            # styles
│   │   ├── App.css            # THE LOOK (Flexbox/Grid layout)
│   │   └── index.css          # global styles
│   │
│   ├── App.tsx            # THE GLUE (Combines Sidebar + CubeCanvas)
│   └── main.tsx           # THE START