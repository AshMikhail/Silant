import { useState, useEffect } from 'react';
import { useAuth } from '../../Context/AuthProvider';
import { useNavigate } from 'react-router-dom';

import './login.css'
import axios from "axios";


export default function Login() {
    const { isAuth, setIsAuth } = useAuth()

    const [login, setLogin]=useState('');
    const [password, setPassword]=useState('');
    const navigate = useNavigate();

    useEffect(() => {
    if (isAuth) {
      navigate('/');
    }
    }, [isAuth, navigate]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/accounts/token/auth/',
                data: {
                    username: login,
                    password: password,
                }
            })
            localStorage.setItem('Token', response?.data?.token);
            localStorage.setItem('CompanyName', response?.data?.company_name);
            localStorage.setItem('сategory', response?.data?.сategory);
            localStorage.setItem('company_id', response?.data?.company_id);
            localStorage.setItem('user_id', response?.data?.user_id);
            setIsAuth(true);
            navigate('/');

        } catch (err) {
            console.log(err.message);
        }
    }

    const handleLoginChange = (e) => {
    const input = e.target.value;
    setLogin(input);
    };

    const handlePasswordChange = (e) => {
    const input = e.target.value;
    setPassword(input);
    };

    return (
        <form className="login-form" onSubmit={handleSubmit}>
            <label htmlFor="username">Логин:</label>
            <input
                type="text"
                id="username"
                autoComplete="on"
                value={login}
                onChange={handleLoginChange}
                required
            />
            <label htmlFor="password">Пароль:</label>
            <input
                type="password"
                id="password"
                onChange={handlePasswordChange}
                value={password}
                required
            />
            <button className="login-button" type="submit" disabled={!login || !password}>Войти</button>
        </form>

    );
}
