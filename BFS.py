from collections import deque


class CustomerService:
    def __init__(self):
        self.ticket_queue = deque()  
    
    
    def add_ticket(self, ticket):
        self.ticket_queue.append(ticket)
        print(f"Ticket '{ticket}' has been added to the queue.")
    
    
    def process_tickets(self):
        if not self.ticket_queue:
            print("No tickets to process.")
        else:
            while self.ticket_queue:
                current_ticket = self.ticket_queue.popleft()  
                print(f"Processing ticket: {current_ticket}")


service = CustomerService()


service.add_ticket("Ticket #1: Billing issue")
service.add_ticket("Ticket #2: Technical support")
service.add_ticket("Ticket #3: Account login problem")

print("\nStarting to process tickets...\n")


service.process_tickets()
