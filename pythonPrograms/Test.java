import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * Service class for handling user operations.
 */
@Service
public class Test {

    // Class-level annotation: Spring's Service annotation marks this class as a service bean.
    
    private final UserRepository userRepository;

    /**
     * Constructor to inject the UserRepository dependency.
     * Constructor-level annotation: @Autowired tells Spring to automatically
     * wire the UserRepository bean to this class.
     */
    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    /**
     * Method-level annotation: @Transactional marks this method as requiring a transaction.
     * This ensures that the method’s operations are executed in a single transaction.
     */
    @Transactional
    public void addUser(User user) {
        // Method to add a new user to the database
        userRepository.save(user);
    }

    /**
     * Method-level annotation: @Transactional ensures that this method is executed in a transaction context.
     */
    @Transactional(readOnly = true)
    public User getUserById(Long id) {
        // Fetches a user by their ID
        return userRepository.findById(id).orElse(null);
    }

    /**
     * Another method with an annotation: @Transactional and a custom logic.
     */
    @Transactional
    public void updateUser(Long id, User updatedUser) {
        // Update user logic
        User existingUser = userRepository.findById(id).orElse(null);
        if (existingUser != null) {
            existingUser.setName(updatedUser.getName());
            existingUser.setEmail(updatedUser.getEmail());
            userRepository.save(existingUser);
        }
    }

    /**
     * This method does not require a transaction, hence no annotation is needed.
     */
    public void deleteUser(Long id) {
        // Deletes a user by their ID
        userRepository.deleteById(id);
    }
}
