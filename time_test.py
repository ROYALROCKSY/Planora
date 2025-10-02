# from planora_app.dashboard.cards_services import calculate_best_time

# if __name__ == "__main__":
#     # Replace with your actual dummy user_id string
#     user_id = "68dc37187ffd67372e424594"

#     result = calculate_best_time(user_id)
#     print("Best time to study:", result)


# time_test.py
from planora_app.dashboard.cards_services import calculate_best_time

# Replace with your dummy user id
user_id = "68dc37187ffd67372e424595"

# Call function with debug=True to see session details and bucket counts
result = calculate_best_time(user_id, debug=True)

print("\n=== Best Time Calculation Result ===")
print("Best time to study:", result["best_time"])

# Show all session start–end times used
print("\nSessions used for calculation:")
for s in result.get("sessions_used", []):
    print(" -", s)

# Show bucket counts for analysis
print("\nBucket counts (0–95 = 15-min intervals from 0:00 to 23:45):")
print(result.get("bucket_counts", []))

# Highlight the chosen 2-hour bucket window (optional)
if "bucket_counts" in result:
    buckets = result["bucket_counts"]
    max_sum = 0
    max_start = 0
    for start in range(len(buckets) - 7):  # 8 buckets = 2 hours
        window_sum = sum(buckets[start:start + 8])
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = start
    print("\nMost active 2-hour window is approx from bucket", max_start, "to", max_start + 7)
