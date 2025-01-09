import Logotype from './Logotype.svg'
import { useAuth } from '../../Context/AuthProvider';
import './header.css'
import {useNavigate} from "react-router-dom";


function Header() {

    const { isAuth, setIsAuth } = useAuth()
    const navigate = useNavigate();

    const handleLogout = () => {
    setIsAuth(false);
    navigate('/');
    localStorage.removeItem('Token');
    localStorage.removeItem('user_id');
    localStorage.removeItem('сategory');
    localStorage.removeItem('company_id');
    localStorage.removeItem('CompanyName');
    };

    return (
        <header>
            <img className="logo" src={Logotype}/>

            <p className="headerContacts">+7-8352-20-12-09, telegram</p>
            {isAuth ?
            <a className="authButton" href="#" onClick={handleLogout}>Выйти</a>
            :
            <a className="authButton" href="/login">Войти</a>
            }
            <h2 className="headerText">Электронная сервисная книжка "Мой Силант"</h2>
        </header>
    );
  }
  
  export default Header;