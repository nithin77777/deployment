import { useState } from "react";
import "./App.css";

import CustomCards from "./components/MyCard.jsx"
import { Button } from "@mui/material";


function App() {
	const [count, setCount] = useState(0);

	function counter(){
		let cnt = count;
		setCount(cnt+=1);
		console.log(`count is ${count}`);
		
		return count;
	}

	return (
		<>
			<div className="title-main">
				<h1>Nithin Sai Krishna's Portfolio ...</h1>
				<CustomCards/>
				<Button onClick={counter}>Click Here</Button>
				
        
			</div>

			
		</>
	);
}

export default App;
