import { createBrowserRouter } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import WaterAssets from "./pages/WaterAssets"
import Error from './pages/Error'
import WaterAssetDetail from "./pages/WaterAssetDetail";
import Contact from "./pages/Contact";

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                index: true,
                element: <Home />
            },
            {
                path: 'waterassets',
                element: <WaterAssets />
            },
            {
                path: 'waterassets/:id',
                element: <WaterAssetDetail />
            },
            {
                path: 'contact',
                element: <Contact/>
            },
            {
                path: '*',
                element: <Error />
            }
        ]
    }
])

export default router;
