# 🚀 EC2 Monitoring & Auto-Healing System (AWS)

## 📌 Project Overview

This project demonstrates a real-world cloud monitoring and auto-remediation system using AWS services.

It automatically detects high CPU usage on an EC2 instance and triggers a reboot to recover the system.

---

## 🧠 Architecture

EC2 → CloudWatch → SNS → Lambda → EC2 (Reboot)

---

## ⚙️ Services Used

* Amazon EC2
* Amazon CloudWatch
* Amazon SNS
* AWS Lambda
* IAM

---

## 🔥 Features

* Real-time CPU monitoring
* CloudWatch alarms for threshold breach
* Email notifications using SNS
* Automatic EC2 reboot using Lambda
* Self-healing infrastructure

---

## 🧪 Testing

Simulated high CPU load using:

```bash
stress --cpu 2 --timeout 300
```

---

## ✅ Outcome

* Alarm triggered successfully
* SNS notification received
* Lambda executed
* EC2 instance rebooted automatically

---

## 🎯 Use Case

This system can be used in production environments to:

* Prevent downtime
* Automate recovery
* Reduce manual intervention
---
## Screenshots 

# Project workflow Diagram 
<img width="2816" height="1536" alt="Workflow Cloud Monitaring" src="https://github.com/user-attachments/assets/f39bac14-d75c-4a86-a0ac-bcb66eafc028" />

# High-CPU-Alarm
<img width="1920" height="1080" alt="Screenshot (209)" src="https://github.com/user-attachments/assets/8407c1c6-74cb-4089-b46a-5a8cd95a61b1" />

# Logs
<img width="1920" height="1080" alt="Screenshot (210)" src="https://github.com/user-attachments/assets/80bdda55-235a-4fd8-a88c-71ef22237bff" />

# EC2-Monitoring-Dashboard
<img width="1920" height="1080" alt="Screenshot (211)" src="https://github.com/user-attachments/assets/c2f16a76-993c-40b6-b85e-4877dc884cb7" />

---

## 👨‍💻 Author

Siddharth Arekar
