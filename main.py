import sys
import function as func


command = sys.argv[1]

# func.fellows_details()
if command == "borrow":
    func.borrow_item()