import React, { useState } from 'react';
import { api } from '../services/api';

export const DocumentUpload: React.FC = () => {
  const [status, setStatus] = useState<string>('');
  const [uploading, setUploading] = useState<boolean>(false);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files || e.target.files.length === 0) return;
    const file = e.target.files[0];
    
    setUploading(true);
    setStatus('Uploading and embedding vectors...');
    
    try {
      await api.documents.upload(file);
      setStatus(`Successfully parsed and synchronized: ${file.name} ✅`);
    } catch (err) {
      setStatus('Failed to upload document to RAG pipeline. ❌');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div style={{ background: '#222', border: '1px solid #333', borderRadius: '8px', padding: '20px', marginBottom: '20px' }}>
      <h4 style={{ margin: '0 0 10px 0' }}>📄 Train Assistant with New Policy Data</h4>
      <input type="file" accept=".pdf,.txt,.docx" onChange={handleFileChange} disabled={uploading} style={{ color: '#ccc' }} />
      {status && <p style={{ fontSize: '13px', color: '#aaa', marginTop: '10px', margin: '10px 0 0 0' }}>{status}</p>}
    </div>
  );
};