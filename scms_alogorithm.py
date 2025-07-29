def network_device_detection(custom_scripts_enabled=False):
    """
    Unified Network Device Detection Algorithm
    Args:
        custom_scripts_enabled (bool): Whether to run custom scripts
    Returns:
        dict: Test results with device information
    """
    results = {
        'success': False,
        'devices': [],
        'system_resources': None,
        'report': None
    }

    # 1. Initialize test network
    initialize_test_network()

    # 2. Attempt automatic detection
    device_detected = automatic_detection()

    if device_detected:
        # Automatic path
        device = {
            'detected_automatically': True,
            'risk_score': calculate_risk_score(),
            'cloud_connected': verify_cloud_connectivity(),
            'data_formatted': format_data(),
            'nmap_script_executed': execute_nmap_script()
        }
    else:
        # Manual path
        device = add_device_manually()
        device.update({
            'detected_automatically': False,
            'risk_score': calculate_risk_score(),
            'cloud_connected': verify_cloud_connectivity(),
            'nmap_script_executed': execute_nmap_script(),
            'data_formatted': format_data()
        })

    # Common operations
    device['system_resources'] = monitor_resources()
    
    if custom_scripts_enabled:
        device['custom_scripts_run'] = run_custom_scripts()
    
    device['detection_status'] = 'successful'
    results['devices'].append(device)

    # Generate report
    results['report'] = generate_report()
    results['success'] = True

    return results


# Helper functions
def initialize_test_network():
    print("Initializing test network...")

def automatic_detection():
    print("Attempting automatic detection...")
    # Return True if device detected, False otherwise
    return True  # In real implementation, this would be dynamic

def calculate_risk_score():
    print("Calculating risk score...")
    return 75  # Example value

def verify_cloud_connectivity():
    print("Verifying cloud connectivity...")
    return True

def format_data():
    print("Formatting data...")
    return "Formatted data"

def monitor_resources():
    print("Monitoring system resources...")
    return {'cpu': 35, 'memory': 45, 'network': 20}

def execute_nmap_script():
    print("Executing NMAP script...")
    return "NMAP results"

def add_device_manually():
    print("Adding device manually...")
    return {'id': 'manual_device_001', 'type': 'manual'}

def run_custom_scripts():
    print("Running custom scripts...")
    return "Custom script results"

def generate_report():
    print("Generating test report...")
    return "Comprehensive test report"

# Example usage
if __name__ == "__main__":
    test_results = network_device_detection(custom_scripts_enabled=True)
    print("\nTest Results:")
    print(test_results)