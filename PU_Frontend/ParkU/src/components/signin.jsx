import React, { useState, useRef, useEffect } from "react";
import { gsap } from "gsap";

export default function Signin() {
  const [signupMode, setSignupMode] = useState(false);
  const leftRef = useRef(null);
  const rightRef = useRef(null);
  const firstRun = useRef(true);

  useEffect(() => {
    gsap.from(".auth-container", { opacity: 100, y: 30, duration: 0.8, ease: "power3.out" });

    if (firstRun.current) {
      gsap.set(leftRef.current, { width: signupMode ? "15%" : "70%" });
      gsap.set(rightRef.current, { width: signupMode ? "85%" : "60%" });
      firstRun.current = false;
      return;
    }

    if (signupMode) {
      gsap.to(leftRef.current, { width: "15%", duration: 0.8, ease: "power3.inOut" });
      gsap.to(rightRef.current, { width: "85%", duration: 0.8, ease: "power3.inOut" });
      gsap.from(".signup-field", { opacity: 100, y: 16, stagger: 0.06, delay: 0.35, duration: 0.4 });
    } else {
      gsap.to(leftRef.current, { width: "70%", duration: 0.8, ease: "power3.inOut" });
      gsap.to(rightRef.current, { width: "60%", duration: 0.8, ease: "power3.inOut" });
    }
  }, [signupMode]);

  const inputStyle =
    "w-full p-3 rounded-xl bg-white/10 border border-white/20 backdrop-blur-lg text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-400 focus:border-teal-400 transition";

  const btnPrimary =
    "w-full p-3 rounded-xl bg-gradient-to-r from-teal-500 to-green-400 hover:scale-[1.03] hover:shadow-lg shadow-teal-500/50 text-white font-semibold transition";

  const btnOutline =
    "border-2 border-white px-6 py-2 rounded-xl hover:bg-white hover:text-[#3A506B] font-semibold transition";

  const InputField = ({ className = "", ...props }) => (
    <input
      className={`signup-field ${inputStyle} ${className}`}
      {...props}
    />
  );

  return (
    <div className="h-screen w-screen flex overflow-hidden font-poppins bg-gradient-to-br from-[#0f0f0f] via-[#1a1a1a] to-[#2e2e2e]">
      {/* LEFT PANEL */}
      <div
        ref={leftRef}
        className="relative flex items-center justify-center bg-gradient-to-br from-[#1f2933] to-[#323f4b] text-white shadow-2xl 
        transition-all duration-500 ease-in-out"
        style={{
          clipPath: signupMode
            ? "ellipse(80% 100% at 0% 50%)"
            : "ellipse(140% 100% at 0% 50%)",
        }}
        onClick={() => {
          if (signupMode) setSignupMode(false);
        }}
      >
        <div className="absolute top-4 left-5">
          <img 
            src="/logo.png" 
            alt="Logo" 
            className="h-35 w-auto object-contain"
          />
        </div>

        {!signupMode && (
          <div
            className="auth-container w-[80%] max-w-md bg-white/10 backdrop-blur-lg rounded-3xl p-8 shadow-xl"
            onClick={(e) => e.stopPropagation()}
          >
            <h2 className="text-3xl font-bold mb-6">Welcome Back</h2>
            <InputField type="email" placeholder="ID" />
            <InputField type="password" placeholder="Password" className="mt-3" />
            <button className={`${btnPrimary} mt-4`}>Sign In</button>
            <p className="mt-4 text-sm opacity-80 cursor-pointer hover:underline">
              Forgot your password?
            </p>
          </div>
        )}
      </div>

      {/* RIGHT PANEL */}
      <div
        ref={rightRef}
        className="flex items-center justify-center bg-gradient-to-br from-[#2d3748] to-[#4a5568] text-white shadow-2xl 
        transition-all duration-500 ease-in-out"
        style={{
          clipPath: signupMode
            ? "ellipse(140% 100% at 100% 50%)"
            : "ellipse(80% 100% at 100% 50%)",
        }}
      >
        {!signupMode ? (
          <div className="text-center px-6">
            <h1 className="text-3xl font-bold mb-3 tracking-wide">Welcome</h1>
  
            <p className="text-xl font-medium text-gray-200 mb-2">New here?</p>
  
            <p className="text-lg text-gray-400 mb-1">
              Take a minute to set up your account.
            </p>
            <p className="text-lg text-gray-400 mb-6">
              Start booking with ease today.
            </p>
            <button className={btnOutline} onClick={() => setSignupMode(true)}>
              Sign Up
            </button>
          </div>
        ) : (
          <div
            className="auth-container w-[85%] max-w-3xl bg-white/10 backdrop-blur-lg rounded-3xl p-8 shadow-xl"
            onClick={(e) => e.stopPropagation()}
          >
            <h2 className="text-3xl font-semibold mb-6">Create Your Account</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <InputField placeholder="First name" />
              <InputField placeholder="Last name" />
              <InputField
                type="email"
                placeholder="GSuite email"
                className="md:col-span-2"
              />
              <InputField
                placeholder="Department"
                className="md:col-span-2"
              />
              <InputField type="password" placeholder="Create password" />
              <InputField placeholder="Car number plate" />
              <InputField
                placeholder="brand"
                className="md:col-span-2"
              />
            </div>
            <button className={`${btnPrimary} mt-6 animate-pulse hover:animate-none`}>
              Sign Up
            </button>
            <p className="text-xs opacity-80 mt-3">
              Click the left edge to go back to sign in.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
