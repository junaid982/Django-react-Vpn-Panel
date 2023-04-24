import logo from './Images/Logo/favicon.ico';
import './App.css';
import Navbar from './components/Navbar';
import SignIn from './components/Authentication/SignIn';


function App() {
  return (
    <>
    <Navbar logo={logo} />
    
    <SignIn />
    </>
  );
}

export default App;
