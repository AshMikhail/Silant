import React from 'react';
import axios from 'axios'

import './machinelist.css';
import {useAuth} from "../../Context/AuthProvider";


export default function Machinelist() {

    const { isAuth } = useAuth()
    const { companyName } = useAuth()
    const { category } = useAuth()

    const [isLoading, setLoading] = React.useState(true);
    const [machines, setMachines] = React.useState([]);

    const getMachines = () => {
      axios.get(`http://127.0.0.1:8000/api/machine/`).then(resp => {
        setMachines(resp.data);
        setLoading(false);
      });
    }
    React.useEffect(() => {
        getMachines()
    }, []);


    const [value, setValue] = React.useState('');

    const search = machines.filter(machine => {
        return machine.factory_number.toLowerCase().includes(value.toLowerCase());
    });

    const companyFilter = machines.filter(machine => {
        if (category === 'Сервисные компании') {
            return machine.service_company.toLowerCase().includes(companyName.toLowerCase());
        } else if(category === 'Клиент'){
            return machine.client.toLowerCase().includes(companyName.toLowerCase());
        } else {
            return machine
        }

    })


    if (isLoading) {
        return <div className='content_block'><h1>Loading...</h1></div>;
          }

          return (
          <div className='content_block'>
              { isAuth ?
                  <>
                      <h1>{category}: {companyName}</h1>
                      <p>Информация о комплектации и технических характеристиках Вашей техники</p>
                          <div className="linkButton">
                              <a className="UserAuthBtn" href={`/`}>Общая информация</a>
                              <a className="UserAuthBtn" href={'/Maintenances'}>Техн. Обслуживание</a>
                              <a className="UserAuthBtn" href="#">Рекламации</a>
                          </div>
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
                          {
                              companyFilter.map((name) =>
                                  <tr key={name.id}>
                                      <td><a href={`/machine/${name.id}`}>{name.factory_number}</a></td>
                                      <td>{name.technique_model}</td>
                                      <td>{name.engine_model}</td>
                                      <td>{name.engine_number}</td>
                                      <td>{name.transmission_model}</td>
                                      <td>{name.transmission_number}</td>
                                      <td>{name.model_drive_bridge}</td>
                                      <td>{name.number_drive_bridge}</td>
                                      <td>{name.model_controlled_bridge}</td>
                                      <td>{name.number_controlled_bridge}</td>
                                  </tr>
                              )
                          }
                          </tbody>
                      </table>
                  </>
                  :
                  <>
                      <h2>Проверьте комплектацию и технические характеристики техники Силант</h2>
                      <form>
                          <label htmlFor="search">Заводской номер:</label>
                          <input
                              type="text"
                              id="search"
                              autoComplete="on"
                              // value={}
                              onChange={(e) => setValue(e.target.value)}
                              required
                          />
                      </form>
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
                          {
                              search.map((name) =>
                                  <tr key={name.id}>
                                      <td>{name.factory_number}</td>
                                      <td>{name.technique_model}</td>
                                      <td>{name.engine_model}</td>
                                      <td>{name.engine_number}</td>
                                      <td>{name.transmission_model}</td>
                                      <td>{name.transmission_number}</td>
                                      <td>{name.model_drive_bridge}</td>
                                      <td>{name.number_drive_bridge}</td>
                                      <td>{name.model_controlled_bridge}</td>
                                      <td>{name.number_controlled_bridge}</td>
                                  </tr>
                              )
                          }
                          </tbody>
                      </table>

                  </>
              }
        </div>
    );
}
