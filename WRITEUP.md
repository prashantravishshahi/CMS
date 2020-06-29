# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

| | VM  |  App service|
| - | - | - |
| Product to Compare| **Memory optimized—Ev3: High memory-to-core ratio**: Ev3 is latest generation memory-optimized VMs powered by Intel® Xeon® Processors. It is great for relational database servers, caches, and in-memory analytics. |  **ISOLATED: High-Performance, Security and Isolation**: Another level of abstraction for a better user experience.|
| Costs per Hour |  $0.016/hour: The price is very low as compared to App service. But, we have to invest more time and effort to make our app up and running on VM.	 | $0.38/hour : If we don't want to waste time on Platform management, then only App service is the feasible option.|
| Scalability | Scalable | Scalable |
| Availability| Traffic manager | Traffic manager  |
| Workflow |Developer has full control | Easy to create and deploy |

The decision to choose between VM and App Service would be based on above comparison.

I choose App service over VM because it provides quick development and testing turnaround time. As a developer, I am only concerned about my program and not the enviroment setup.

---
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If the requirement is not freezed at the beginning of development cycle, then I would have gone for VM, because it would give me flexibility to change the architecture without modify the Azure objects.

If the cost is major factor for organization and they are not likely to pay for App Service, then I may have chosen VM.


---
### References
https://azure.microsoft.com/en-us/pricing/details/virtual-machines/windows/
https://azure.microsoft.com/en-us/pricing/details/app-service/linux/
