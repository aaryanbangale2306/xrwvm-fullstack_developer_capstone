import React, { useState } from "react";
import "./Register.css";

function Register() {
    const [userName, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");

    const gohome = () => {
        if (typeof window !== "undefined") {
            window.location.href = window.location.origin;
        }
    };

    const handleRegister = async (event) => {
        event.preventDefault();

        const rootUrl = typeof window !== "undefined" ? window.location.origin : "";
        const registerUrl = `${rootUrl}/djangoapp/register`;

        try {
            const res = await fetch(registerUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    userName: userName,
                    password: password,
                    firstName: firstName,
                    lastName: lastName,
                    email: email,
                }),
            });

            const json = await res.json();
            if (json.status === "Authenticated" || json.status) {
                if (typeof sessionStorage !== "undefined") {
                    sessionStorage.setItem("username", json.userName);
                }
                if (typeof window !== "undefined") {
                    window.location.href = window.location.origin;
                }
            } else if (json.error === "Already Registered") {
                if (typeof alert !== "undefined") {
                    alert("The user with same username is already registered");
                }
            } else {
                if (typeof alert !== "undefined") {
                    alert(json.error || "Registration failed");
                }
            }
        } catch (error) {
            console.error("Registration error:", error);
            if (typeof alert !== "undefined") {
                alert("Registration failed. Please try again.");
            }
        }
    };

    return (
        <div className="register_container register-container">
            <div className="header">
                <span className="text">Sign-up</span>
            </div>

            <form onSubmit={handleRegister}>
                <div className="inputs">
                    <div className="input_group">
                        <label htmlFor="username">Username</label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            placeholder="Username"
                            className="input_field"
                            value={userName}
                            onChange={(e) => setUserName(e.target.value)}
                            required
                        />
                    </div>

                    <div className="input_group">
                        <label htmlFor="firstName">First Name</label>
                        <input
                            type="text"
                            id="firstName"
                            name="firstName"
                            placeholder="First Name"
                            className="input_field"
                            value={firstName}
                            onChange={(e) => setFirstName(e.target.value)}
                            required
                        />
                    </div>

                    <div className="input_group">
                        <label htmlFor="lastName">Last Name</label>
                        <input
                            type="text"
                            id="lastName"
                            name="lastName"
                            placeholder="Last Name"
                            className="input_field"
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                            required
                        />
                    </div>

                    <div className="input_group">
                        <label htmlFor="email">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            placeholder="Email"
                            className="input_field"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    <div className="input_group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            placeholder="Password"
                            className="input_field"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                </div>

                <div className="submit_panel">
                    <button type="submit" className="submit" id="register-btn">
                        Register
                    </button>
                </div>
            </form>
        </div>
    );
}

export default Register;