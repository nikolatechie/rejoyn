import React, { useState } from "react";

const TripForm: React.FC = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [loading, setLoading] = useState(false)
  const [topDestinations, setTopDestinations] = useState([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    console.log(startDate, endDate);
    setLoading(true);

    try {
      const response = await fetch(`http://0.0.0.0:8000/top-destinations?group_id=0`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      setLoading(false);
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
        width: "80%",
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
      {loading && <h3 style={{ marginTop: "80px" }}>Finding a perfect holiday for your group...</h3>}
      {topDestinations.length > 0 && (
        <div style={{ marginTop: "40px" }}>
          <h3>Top Destinations:</h3>
          <ul style={{ marginTop: "40px" }}>
            {topDestinations.map((destination, index) => (
              <li key={index} style={{ marginBottom: "20px" }}>
                <strong>{index + 1}</strong><br />
                <strong>Destination:</strong> {destination["en-GB"]} <br />
                <strong>Score:</strong> {(parseFloat(destination['score']) * 100).toFixed(0)}%<br />
                <strong>Description:</strong> {destination['description']} <br />
                <strong>Vibes:</strong> {Object.keys(destination['vibes'])
                  .filter((key) => destination['vibes'][key] === "1")
                  .map((key) => key.replace(/_/g, " "))
                  .join(", ")}.
                <br />
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default TripForm;
