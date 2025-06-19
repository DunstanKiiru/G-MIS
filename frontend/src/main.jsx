import React from 'react'
import ReactDOM from 'react'
import { RouterProvider } from "react-router-dom"
import route from './route'

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AuthProvider>
      <RouterProvider router={route} />
    </AuthProvider>
  </React.StrictMode>
);
