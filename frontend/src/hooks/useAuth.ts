import { useState, useEffect } from 'react';
import { api } from '../services/api';

export function useAuth() {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const token = localStorage.getItem('token');
    setIsAuthenticated(!!token);
    setLoading(false);
  }, []);

  const login = async (username: string, password: string) => {
    await api.auth.login(username, password);
    setIsAuthenticated(true);
  };

  const logout = () => {
    api.auth.logout();
    setIsAuthenticated(false);
  };

  return { isAuthenticated, loading, login, logout };
}