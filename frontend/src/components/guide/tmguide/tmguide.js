import './tmguide.css'
import React from "react";
import axios from "axios";

const [techModel, setTechModel] = React.useState();

export default function Tmguide() {


    React.useEffect(() => {
      axios.get(`${baseURL}guide/tm/`).then(resp => {
        setTechModel(resp.data);
        console.log(resp.data);
      });
    }, []);

    return (
        <div className="tmguide">
            <h1>{guide.name} </h1>
            <h2>{guide.description}</h2>
        </div>
    );
}
