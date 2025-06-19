import React from 'react'
import ReactDOM from 'react'
import { RouterProvider } from "react-router-dom"
import route from './routes'

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
      <RouterProvider router={route} />
  </React.StrictMode>
);
