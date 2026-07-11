import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/chatWindow';
import DocumentUpload from './components/DocumentUpload';

function App() {
  const [activeTab, setActiveTab] = useState<'chat' | 'upload'>('chat');

  return (
    <div className="flex h-screen bg-slate-900 text-white">
      {/* Sidebar navigation */}
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {activeTab === 'chat' ? (
          <ChatWindow />
        ) : (
          <DocumentUpload />
        )}
      </main>
    </div>
  );
}

export default App;