
import { createBrowserRouter } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import WaterAssets from "./pages/WaterAssets"
import Error from './pages/Error'
import WaterAssetDetail from "./pages/WaterAssetDetail";
import Contact from "./pages/Contact";
import CommunityContributions from "./pages/CommunityContributions";
import OMVisits from "./pages/OMVisits";
import SparePartsInventory from "./pages/SparePartsInventory";
import StaffDevelopment from "./pages/StaffDevelopment";
import WaterQualityTests from "./pages/WaterQualityTests";
import Login from "./pages/Login";
import Register from "./pages/Register";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      {
        path: "waterassets",
        element: <WaterAssets />,
      },
      {
        path: "waterassets/:id",
        element: <WaterAssetDetail />,
      },
      {
        path: "login",
        element: <Login />,
      },
      {
        path: "register",
        element: <Register />,
      },
      {
        path: "contact",
        element: <Contact />,
      },
      {
        path: "*",
        element: <Error />,
      },
      {
        path: "omvisits",
        element: <OMVisits />,
      },
      {
        path: "communitycontributions",
        element: <CommunityContributions />,
      },
      {
        path: "staffdevelopment",
        element: <StaffDevelopment />,
      },
      {
        path: "sparepartsinventory",
        element: <SparePartsInventory />,
      },
      {
        path: "waterquality",
        element:<WaterQualityTests/>
      }
    ],
  },
]);

export default router;
