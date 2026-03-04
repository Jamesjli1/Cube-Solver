// Basic button for sidebar

interface ButtonProps {
  label: string;
  onClick: () => void;
}

export default function Button({ label, onClick }: ButtonProps) {
  return (
    <button className="cube-button" onClick={onClick}>
      {label}
    </button>
  );
}