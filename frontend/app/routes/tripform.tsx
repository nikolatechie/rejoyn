import React, { useState } from "react";

const TripForm: React.FC = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log(startDate, endDate);
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
