import React from "react";

function Sidebar() {
  return (
    <div className="w-64 bg-slate-800 text-white p-4">
      <h2 className="text-xl font-bold">
        Company Policy Assistant
      </h2>

      <button className="mt-5 w-full bg-blue-600 p-2 rounded">
        Chat
      </button>

      <button className="mt-3 w-full bg-green-600 p-2 rounded">
        Upload Document
      </button>
    </div>
  );
}

export default Sidebar;