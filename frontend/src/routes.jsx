import { createBrowserRouter } from "react-router-dom";
import Home from "./pages/Home";
import WaterAssets from "./pages/WaterAssets"
import Error from './pages/Error'

const router = createBrowserRouter([
    {
        path: '/',
        element: <Home/>
    },
    {
        path: '/waterassets',
        element: <WaterAssets />
    },
    {
        path: '*',
        element: <Error />
    }
])

export default router;
