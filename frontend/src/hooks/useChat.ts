import { useState } from 'react';
import { api } from '../services/api';

export interface Message {
  role: 'user' | 'assistant' | 'system';
  text: string;
}

export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false);

  const sendMessage = async (text: string) => {
    if (!text.trim()) return;

    const userMsg: Message = { role: 'user', text };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);

    try {
      const data = await api.chat.ask(text);
      const assistantMsg: Message = { role: 'assistant', text: data.response || "Success!" };
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err) {
      setMessages((prev) => [...prev, { role: 'system', text: 'Error connecting to vector storage or AI engine.' }]);
    } finally {
      setLoading(false);
    }
  };

  return { messages, loading, sendMessage };
}