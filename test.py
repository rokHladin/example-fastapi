import asyncio

async def example_task():
    print("Task started")
    await asyncio.sleep(2)  # Simulate an asynchronous operation that takes 2 seconds
    print("Task completed")

async def main():
    print("Main program started")
    
    # Start the asynchronous task
    task = asyncio.create_task(example_task())
    
    # While the task is running, the program can continue executing other code
    for i in range(5):
        print(f"Main program is running ({i+1}/5)")
        await asyncio.sleep(1)  # Simulate other work
    
    # Wait for the task to complete
    await task
    
    print("Main program completed")

# Run the main function
asyncio.run(main())
