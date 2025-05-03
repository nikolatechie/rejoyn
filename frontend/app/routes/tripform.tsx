import React, { useState } from "react";

const TripForm: React.FC = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [topDestinations, setTopDestinations] = useState([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    console.log(startDate, endDate);

    try {
      const response = await fetch(`http://0.0.0.0:8000/top-destinations?group_id=0`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      if (response.ok) {
        // success
        console.log("success");
        console.log(data);
        setTopDestinations(data.top_destinations);
      } else {
        console.log("fail");
        // alert(data.errorMessage);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div
      style={{
        maxWidth: "50%",
        margin: "auto",
        marginTop: "100px",
      }}
    >
      <h1 className="mb-4">Plan Your Trip</h1>
      <div className="mb-3">
        <label htmlFor="startDate" className="form-label">
          Start Date
        </label>
        <input
          type="date"
          className="form-control"
          id="startDate"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          min={new Date().toISOString().split("T")[0]} // Set minimum date to today
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="endDate" className="form-label">
          End Date
        </label>
        <input
          type="date"
          className="form-control"
          id="endDate"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          required
        />
      </div>
      <div className="text-end">
        <button type="submit" className="btn btn-primary" onClick={handleSubmit}>
          Get recommendations
        </button>
      </div>
    </div>
  );
};

export default TripForm;
