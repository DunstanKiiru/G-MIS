import React from 'react'
import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <div className="container mt-5 text-center">
      <h1>GARUWASCO MIS</h1>
      <p>
        Garissa Rural Water and Sanitation Company — Safe, adequate and sustainable rural water services
      </p>

      <div className = "my-4">
        <Link to ="/waterassets" className='btn tbn-primary btn-lg me-3'>
          View Water Assets
        </Link>

      </div>
    </div>
  );
}

export default Home