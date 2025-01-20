import { createContext, useContext, useState } from 'react';

// Create User Context
const UserContext = createContext(null);

// Provider Component
export function UserProvider({ children }) {
  const [currentUser, setCurrentUser] = useState({id : 1, type: 'influencer',});

  return (
    <UserContext.Provider value={{ currentUser, setCurrentUser }}>
      {children}
    </UserContext.Provider>
  );
}

// Custom Hook to use the User Context
export function useUser() {
  return useContext(UserContext);
}