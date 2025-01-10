import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./Context/AuthProvider";
import Machinelist from "./components/machinelist/machinelist";
import Login from "./components/Auth/login";
import Header from "./components/header/header";
import Machine from "./components/Machine/machine";
import Maintenances from "./components/Maintenance/maintenances";

function App() {

  return (
      <Router>
          <AuthProvider>
              <Header />
              <div className="App">
                <Routes>
                    <Route path="/" element={<Machinelist />} />
                    <Route path="/login" element={<Login />} />
                    <Route exaxt path={'/machine/:machId'} Component={Machine}/>
                    <Route exaxt path={'/Maintenances'} Component={Maintenances}/>
                </Routes>
              </div>
          </AuthProvider>
      </Router>
  );
}

export default App;
