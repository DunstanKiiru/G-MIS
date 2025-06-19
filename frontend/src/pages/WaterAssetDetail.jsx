import {useEffect, useState} from "react"
import { useParams } from "react-router-dom";
import axios from "axios"

function WaterAssetDetail(){
    const {id} = useParams()
    const [asset, setWaterAsset] = useState(null)

    useEffect(() =>{
        axios.get(`/api/assets/${id}`).then((res) => setWaterAsset(res.data))
    }, [id])

    if (!asset) return <p>Asset not found...</p>

    return(
        <div>
            <div>
                <h2 className="mb-3">{asset.name}</h2>
                <p><strong>Type:</strong> {asset.type}</p>
                <p><strong>Status:</strong> {asset.status}</p>
                <p><strong>Location:</strong> {asset.location}</p>
                <p><strong>Material:</strong> {asset.material}</p>
            </div>
        </div>
    )
}

export default WaterAssetDetail;
