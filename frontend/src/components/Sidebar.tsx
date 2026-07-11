import React from 'react';

interface SidebarProps {
  onLogout: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ onLogout }) => {
  return (
    <div style={{ width: '260px', background: '#111', borderRight: '1px solid #333', display: 'flex', flexDirection: 'column', justifyBetween: 'space-between', padding: '20px' }}>
      <div>
        <h3 style={{ margin: '0 0 20px 0', color: '#007acc' }}>📁 Dashboard</h3>
        <p style={{ color: '#aaa', fontSize: '14px' }}>Company Policy Assistant v1.0</p>
      </div>
      <button onClick={onLogout} style={{ width: '100%', background: '#cc3333', color: '#fff', border: 'none', padding: '10px', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>
        Log Out
      </button>
    </div>
  );
};