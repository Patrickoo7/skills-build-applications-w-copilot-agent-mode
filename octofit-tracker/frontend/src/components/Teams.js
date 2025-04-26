import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Teams</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Team Name</th>
            <th>Members</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team, index) => (
            <tr key={index}>
              <td>{team.name}</td>
              <td>{team.members.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary">Add Team</button>
    </div>
  );
};

export default Teams;
