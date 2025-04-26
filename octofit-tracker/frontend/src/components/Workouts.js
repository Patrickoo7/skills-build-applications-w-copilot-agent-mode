import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Workouts</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Workout Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, index) => (
            <tr key={index}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary">Add Workout</button>
    </div>
  );
};

export default Workouts;
