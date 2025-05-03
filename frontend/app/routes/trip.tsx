import { useEffect } from "react"

export default function Trip() {
  useEffect(() => {
    const testApi = async () => {
      try {
        const response = await fetch(
          `http://0.0.0.0:8000/top-destinations?group_id=0`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        // const data = await response.json();
        if (response.ok) {
          // success
          console.log("success");
          // console.log(data);
        } else {
          console.log("fail");
          // alert(data.errorMessage);
        }
      } catch (error) {
        console.log(error)
      }
    }
    testApi();
  }, [])

  return <h2>Trip</h2>
}