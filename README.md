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


---

## 👨‍💻 Author

Siddharth Arekar
