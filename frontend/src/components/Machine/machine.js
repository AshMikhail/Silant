import React from 'react';
import axios from 'axios'

import './machine.css';
import {useNavigate} from "react-router-dom";
import { useParams } from 'react-router-dom';
import {useAuth} from "../../Context/AuthProvider";

const baseURL = "http://127.0.0.1:8000/api/"

export default function Machine() {
    const { isAuth } = useAuth()
    const { companyName } = useAuth()
    const { category } = useAuth()
    const machId = useParams().machId
    const navigate = useNavigate();


    const [isLoading, setLoading] = React.useState(true);
    const [machine, setMachine] = React.useState([]);

      //   React.useEffect(() => {
      //   if (isAuth === false) {
      //     navigate('/');
      //   }
      // }, [isAuth, navigate]);

    const getMachine = () => {
      axios.get(`${baseURL}machine/${machId}/`).then(resp => {
        setMachine(resp.data);
        setLoading(false);
      });
    }
    React.useEffect(() => {
        getMachine()
    }, []);



    if (isLoading) {
        return <div className='content_block'><h1>Loading...</h1></div>;
          }

          return (
          <div className='content_block'>
              { isAuth ?
                  <>
                      <h2>{category}: {companyName}</h2>
                      <p>Информация о комплектации и технических характеристиках Вашей техники</p>
                      <table border="5" width="600" margin="5">
                          <thead>
                          <td>№ Машины</td>
                          <td>Модель</td>
                          <td>Модель двигателя</td>
                          <td>Номер двигателя</td>
                          <td>Модель Трансмиссии</td>
                          <td>Номер Трансмиссии</td>
                          <td>Модель Ведущего Мост</td>
                          <td>Номер Ведущего Моста</td>
                          <td>Модель Управляемого Моста</td>
                          <td>Номер Управляемого Моста</td>
                          </thead>
                          <tbody>
                          <tr key={machine}>
                              <td>{machine.factory_number}</td>
                              <td>{machine.technique_model}</td>
                              <td>{machine.engine_model}</td>
                              <td>{machine.engine_number}</td>
                              <td>{machine.transmission_model}</td>
                              <td>{machine.transmission_number}</td>
                              <td>{machine.model_drive_bridge}</td>
                              <td>{machine.number_drive_bridge}</td>
                              <td>{machine.model_controlled_bridge}</td>
                              <td>{machine.number_controlled_bridge}</td>
                          </tr>
                          </tbody>
                      </table>
                  </>
                  :
                  <>
                      <h2>{companyName}</h2><h1>{category}</h1>
                      <p>Информация о комплектации и технических характеристиках Вашей техники</p>
                      <table border="5" width="600" margin="5">
                          <thead>
                          <td>№ Машины</td>
                          <td>Модель</td>
                          <td>Модель двигателя</td>
                          <td>Номер двигателя</td>
                          <td>Модель Трансмиссии</td>
                          <td>Номер Трансмиссии</td>
                          <td>Модель Ведущего Мост</td>
                          <td>Номер Ведущего Моста</td>
                          <td>Модель Управляемого Моста</td>
                          <td>Номер Управляемого Моста</td>
                          </thead>
                          <tbody>
                          <tr key={machine}>
                              <td>{machine.factory_number}</td>
                              <td>{machine.technique_model}</td>
                              <td>{machine.engine_model}</td>
                              <td>{machine.engine_number}</td>
                              <td>{machine.transmission_model}</td>
                              <td>{machine.transmission_number}</td>
                              <td>{machine.model_drive_bridge}</td>
                              <td>{machine.number_drive_bridge}</td>
                              <td>{machine.model_controlled_bridge}</td>
                              <td>{machine.number_controlled_bridge}</td>
                          </tr>
                          </tbody>
                      </table>

                  </>
              }
          </div>
          );
}