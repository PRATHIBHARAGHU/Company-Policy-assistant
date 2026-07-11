import React, { useState } from 'react';
import { Message } from '../hooks/useChat';

interface ChatWindowProps {
  messages: Message[];
  loading: boolean;
  onSendMessage: (text: string) => void;
}

export const ChatWindow: React.FC<ChatWindowProps> = ({ messages, loading, onSendMessage }) => {
  const [input, setInput] = useState('');

  const submit = () => {
    if (!input.trim()) return;
    onSendMessage(input);
    setInput('');
  };

  return (
    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', height: '100%' }}>
      <div style={{ flex: 1, overflowY: 'auto', padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start', maxWidth: '70%' }}>
            <div style={{ background: msg.role === 'user' ? '#007acc' : msg.role === 'system' ? '#444' : '#2d2d2d', padding: '12px 16px', borderRadius: '8px', color: '#fff' }}>
              {msg.text}
            </div>
          </div>
        ))}
        {loading && <div style={{ color: '#888', fontStyle: 'italic' }}>Reading through uploaded policy data...</div>}
      </div>
      <div style={{ padding: '20px', borderTop: '1px solid #333', display: 'flex', gap: '10px' }}>
        <input value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && submit()} placeholder="Ask about remote work, leaves, compliance..." style={{ flex: 1, padding: '12px', background: '#222', border: '1px solid #444', borderRadius: '6px', color: '#fff' }} />
        <button onClick={submit} style={{ padding: '12px 24px', background: '#007acc', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>Send</button>
      </div>
    </div>
  );
};