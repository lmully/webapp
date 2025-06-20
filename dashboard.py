// src/App.jsx
import React from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const dummyServiceAlerts = [
  { id: 1, name: 'Tractor - Service due', due: '25/06/2025' },
  { id: 2, name: 'Chainsaw - Chain replacement', due: '29/06/2025' },
];

const dummySnags = [
  { id: 1, description: 'Slasher belt snapped', asset: 'Slasher', cost: 200, status: 'Open' },
  { id: 2, description: 'West fence fallen', asset: 'Boundary Fence', cost: 500, status: 'In Progress' },
];

const dummyExpenses = [
  { month: 'Jan', cost: 320 },
  { month: 'Feb', cost: 210 },
  { month: 'Mar', cost: 480 },
  { month: 'Apr', cost: 300 },
];

export default function App() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Willowdale Farm Dashboard</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card><CardContent className="p-4">Total Assets: 12</CardContent></Card>
        <Card><CardContent className="p-4">Upcoming Services: {dummyServiceAlerts.length}</CardContent></Card>
        <Card><CardContent className="p-4">Outstanding Snags: {dummySnags.length}</CardContent></Card>
        <Card><CardContent className="p-4">Est. Monthly Cost: $320</CardContent></Card>
      </div>

      <section>
        <h2 className="text-xl font-semibold mt-4 mb-2">Service Alerts</h2>
        <ul className="list-disc pl-5">
          {dummyServiceAlerts.map(service => (
            <li key={service.id}>{service.name} (Due: {service.due})</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold mt-4 mb-2">Snags</h2>
        <ul className="list-disc pl-5">
          {dummySnags.map(snag => (
            <li key={snag.id}>{snag.description} – {snag.asset} – Est. ${snag.cost} – {snag.status}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold mt-4 mb-2">Monthly Expenses</h2>
        <ResponsiveContainer width="100%" height={200}>
          <BarChart data={dummyExpenses}>
            <XAxis dataKey="month" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="cost" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </section>
    </div>
  );
}
