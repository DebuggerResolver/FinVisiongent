# Custom Flow approach for nested flow processing - CORRECTED
from utils.pocketflow import Node, Flow

# Payment Flow Nodes
class ValidatePaymentNode(Node):
    def post(self, shared, prep_res, exec_res):
        print("Payment validation done")
        shared['payment_validated'] = True
        return "default"

class ProcessPayment(Node):
    def post(self, shared, prep_res, exec_res):
        print("Processing payment done")
        shared['payment_processed'] = True
        return "default"

class PaymentConfirmation(Node):
    def post(self, shared, prep_res, exec_res):
        print("Payment confirmation done")
        shared['payment_confirmed'] = True
        return "default"

# Inventory Flow Nodes
class CheckStock(Node):
    def post(self, shared, prep_res, exec_res):
        print("Check stock")
        shared['stock_checked'] = True
        return "default"

class ReserveItems(Node):
    def post(self, shared, prep_res, exec_res):
        print("Items reserved")
        shared['items_reserved'] = True
        return "default"

class UpdateInventory(Node):
    def post(self, shared, prep_res, exec_res):
        print("Inventory updated")
        shared['inventory_updated'] = True
        return "default"

# Shipping Flow Nodes
class CreateLabel(Node):
    def post(self, shared, prep_res, exec_res):
        print("Shipping label created")
        shared['label_created'] = True
        return "default"

class AssignCarrier(Node):
    def post(self, shared, prep_res, exec_res):
        print("Carrier assigned")
        shared['carrier_assigned'] = True
        return "default"

class SchedulePickup(Node):
    def post(self, shared, prep_res, exec_res):
        print("Pickup scheduled")
        shared['pickup_scheduled'] = True
        return "default"

# Custom Flow Classes
class PaymentFlow(Flow):
    def prep(self, shared):
        print("=== Starting Payment Flow ===")
        return {"flow_type": "payment"}
    
    def post(self, shared, prep_res, exec_res):
        print("=== Payment Flow Completed ===")
        print(f"Payment Status: {shared.get('payment_confirmed', False)}")
        return "inventory"  # Signal to move to inventory flow

class InventoryFlow(Flow):
    def prep(self, shared):
        print("=== Starting Inventory Flow ===")
        # Check if payment was completed
        if not shared.get('payment_confirmed', False):
            print("Warning: Payment not confirmed!")
        return {"flow_type": "inventory"}
    
    def post(self, shared, prep_res, exec_res):
        print("=== Inventory Flow Completed ===")
        print(f"Inventory Status: {shared.get('inventory_updated', False)}")
        return "shipping"  # Signal to move to shipping flow

class ShippingFlow(Flow):
    def prep(self, shared):
        print("=== Starting Shipping Flow ===")
        # Check if inventory was processed
        if not shared.get('inventory_updated', False):
            print("Warning: Inventory not updated!")
        return {"flow_type": "shipping"}
    
    def post(self, shared, prep_res, exec_res):
        print("=== Shipping Flow Completed ===")
        print(f"Shipping Status: {shared.get('pickup_scheduled', False)}")
        return "complete"  # Signal completion

# Master Order Pipeline Flow
class OrderPipelineFlow(Flow):
    def prep(self, shared):
        print("🚀 === STARTING ORDER PIPELINE ===")
        shared['order_id'] = "ORD-12345"
        shared['start_time'] = "2024-01-01 10:00:00"
        return {"pipeline": "order_processing"}
    
    def post(self, shared, prep_res, exec_res):
        print("✅ === ORDER PIPELINE COMPLETED ===")
        print("Final Order Status:")
        print(f"  Order ID: {shared.get('order_id')}")
        print(f"  Payment Confirmed: {shared.get('payment_confirmed', False)}")
        print(f"  Inventory Updated: {shared.get('inventory_updated', False)}")
        print(f"  Pickup Scheduled: {shared.get('pickup_scheduled', False)}")
        return "order_complete"

if __name__ == "__main__":
    # Create Payment Flow nodes and chain them
    validate_payment = ValidatePaymentNode()
    process_payment = ProcessPayment()
    payment_confirmation = PaymentConfirmation()
    
    validate_payment >> process_payment >> payment_confirmation
    payment_flow = PaymentFlow(start=validate_payment)
    
    # Create Inventory Flow nodes and chain them
    check_stock = CheckStock()
    reserve_items = ReserveItems()
    update_inventory = UpdateInventory()
    
    check_stock >> reserve_items >> update_inventory
    inventory_flow = InventoryFlow(start=check_stock)
    
    # Create Shipping Flow nodes and chain them
    create_label = CreateLabel()
    assign_carrier = AssignCarrier()
    schedule_pickup = SchedulePickup()
    
    create_label >> assign_carrier >> schedule_pickup
    shipping_flow = ShippingFlow(start=create_label)
    
    # CORRECTED: Connect flows using next() method instead of conditional transitions
    payment_flow.next(inventory_flow, "inventory")
    inventory_flow.next(shipping_flow, "shipping")
    
    # Create the master order pipeline flow
    order_pipeline = OrderPipelineFlow(start=payment_flow)
    
    # Initialize shared data
    shared_data = {
        "customer_id": "CUST-001",
        "order_amount": 99.99,
        "items": ["item1", "item2"]
    }
    
    # Run the entire order pipeline
    print("Starting Order Processing Pipeline...")
    result = order_pipeline.run(shared_data)
    print(f"\nPipeline Result: {result}")
    print(f"Final Shared Data: {shared_data}")