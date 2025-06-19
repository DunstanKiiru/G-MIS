import { createBrowserRouter } from "react-router-dom";
import Home from "./pages/Home";
import WaterAssets from "./pages/WaterAssets"

const router = createBrowserRouter([
    {
        path: '/',
        element: <Home/>
    }
])