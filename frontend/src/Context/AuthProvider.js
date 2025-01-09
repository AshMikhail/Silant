import React from 'react';

const AuthContext = React.createContext();

export const AuthProvider = ({ children }) => {
    const [isAuth, setIsAuth] = React.useState(false);
    const companyName = localStorage.getItem('CompanyName');
    const category  = localStorage.getItem('сategory');
    const userID = localStorage.getItem('user_id');
    const companyId = localStorage.getItem('company_id');

    const checkAuthStatus = () => {
    const accessToken = localStorage.getItem('Token');

    if (!accessToken) {
        console.log("Token expired or not found.");
        setIsAuth(false);
        localStorage.removeItem('Token');
    } else {
        setIsAuth(true);
    }
  };

  React.useEffect(() => {
    checkAuthStatus();
  }, []);

  return (
    <AuthContext.Provider value={{ isAuth, setIsAuth, companyName, category,
    userID, companyId }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => React.useContext(AuthContext);