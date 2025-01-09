import './maintenances.css'
import React from "react";
import axios from "axios";
import {useAuth} from "../../Context/AuthProvider";

export default function Maintenances() {

    const { category } = useAuth()
    const { companyName } = useAuth()

    const [isLoading, setLoading] = React.useState(true);
    const [maintenances, setMaintenances] = React.useState([]);

    const getMaintenances = () => {
      axios.get('http://localhost:8000/api/maintenance/').then(resp => {
        setMaintenances(resp.data);
        console.log(companyName);
        console.log(resp.data)
        setLoading(false);
      });
    }
    React.useEffect(() => {
        getMaintenances()
    }, []);

    // const search = maintenances.filter(mtrs => {
    //     return mtrs.maintenance_company.toLowerCase().include(companyName.toLowerCase());
    // });
        if (isLoading) {
        return <div className='content_block'><h1>Loading...</h1></div>;
          }

    return (
        <div className="maintenances">
            <h1>{category}: {companyName}</h1>
            <p>Информация о комплектации и технических характеристиках Вашей техники</p>
            <div className="linkButton">
                <a className="UserAuthBtn" href={`/`}>Общая информация</a>
                <a className="UserAuthBtn" href={'/Maintenances'}>Техн. Обслуживание</a>
                <a className="UserAuthBtn" href="#">Рекламации</a>
            </div>
            <table border="5" width="600" margin="5">
                <thead>
                    <td>Дата Тех Обслуживания</td>
                    <td>Наработка, м/час</td>
                    <td>№ заказ-наряда</td>
                    <td>Дата заказ-наряда</td>
                    <td>Организация, проводившая Тех Обслуживание</td>
                    <td>Вид Тех Обслуживания</td>
                    <td>Машина</td>
                    <td>Сервисная компания</td>
                </thead>
                <tbody>
                {
                    maintenances.map((name) =>
                        <tr key={name.id}>
                            <td>{name.date_of_maintenance}</td>
                            <td>{name.Operating_time}</td>
                            <td>{name.Order_number}</td>
                            <td>{name.Order_date}</td>
                            <td>{name.maintenance_company}</td>
                            <td>{name.types_of_maintenance}</td>
                            <td>{name.machine}</td>
                            <td>{name.service_company}</td>
                        </tr>
                    )
                }
                </tbody>
            </table>
        </div>
    )
}

