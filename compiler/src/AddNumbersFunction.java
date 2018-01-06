import java.util.*;
import com.google.common.collect.ImmutableSet;
import com.google.template.soy.pysrc.restricted.SoyPySrcFunction;
import com.google.template.soy.pysrc.restricted.PyExpr;

/**
 * Provides a function for adding 2 numbers
 */
public class AddNumbersFunction implements SoyPySrcFunction {

    public PyExpr computeForPySrc(List<PyExpr> args) {
        String code = "'Sum is ' + str(data['n1'] + data['n2'])";
        return new PyExpr(code, Integer.MAX_VALUE);
    }

    public String getName() {
        return "addNumbers";
    }

    public Set<Integer> getValidArgsSizes() {
        return ImmutableSet.of(2);
    }

}
